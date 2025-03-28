
import java.io.*;
import java.net.HttpURLConnection;
import java.net.URL;
import javax.net.ssl.*;
import java.security.NoSuchAlgorithmException;
import java.security.cert.X509Certificate;
import java.util.Base64;

public class PowerScaleFileOperations {

    // 禁用 SSL 驗證
    public static void disableSSLVerification() {
        try {
            // 創建一個信任所有憑證的 TrustManager
            TrustManager[] trustAllCertificates = new TrustManager[]{
                new X509TrustManager() {
                    public X509Certificate[] getAcceptedIssuers() {
                        return null;
                    }

                    public void checkClientTrusted(X509Certificate[] certs, String authType) {
                    }

                    public void checkServerTrusted(X509Certificate[] certs, String authType) {
                    }
                }
            };

            // 創建 SSL 上下文
            SSLContext sc = SSLContext.getInstance("TLS");
            sc.init(null, trustAllCertificates, new java.security.SecureRandom());

            // 設定 SSL 連線工廠
            HttpsURLConnection.setDefaultSSLSocketFactory(sc.getSocketFactory());

            // 設定主機名稱驗證器，讓所有主機都通過驗證
            HttpsURLConnection.setDefaultHostnameVerifier((hostname, session) -> true);
        } catch (Exception e) {
            e.printStackTrace();
        }
    }

    // PowerScale 叢集資訊
    private static String clusterIp = "192.168.55.51:8080";
    private static String username = "admin";
    private static String password = "P@ssw0rd";

    // 基本 URL
    private static String baseUrl = "https://" + clusterIp + "/namespace";

    // 要創建的目錄和子目錄路徑
    private static String directoryPath = "/ifs/TC/dd-1/dd-2";

    // 本地檔案路徑
    private static String localFilePath = "sample.txt";

    // 遠端檔案路徑
    private static String remoteFilePath = directoryPath + "/sample.txt";

    // 創建目錄（包括父目錄）
    public static void createDirectory(String path) {
        try {
            URL url = new URL(baseUrl + path + "?recursive=true");
            HttpURLConnection connection = (HttpURLConnection) url.openConnection();
            connection.setRequestMethod("PUT");
            connection.setRequestProperty("x-isi-ifs-target-type", "container");
            connection.setDoOutput(true);
            connection.setRequestProperty("Authorization", "Basic " + getBasicAuth());

            // 發送請求
            int responseCode = connection.getResponseCode();
            if (responseCode == 200 || responseCode == 201 || responseCode == 204) {
                System.out.println("目錄 " + path + " 創建成功。");
            } else {
                System.out.println("創建目錄失敗，狀態碼：" + responseCode + "，訊息：" + connection.getResponseMessage());
            }
        } catch (IOException e) {
            e.printStackTrace();
        }
    }

    // 上傳檔案
    public static void uploadFile(String remotePath, String localPath, boolean overwrite) {
        try {
            File file = new File(localPath);
            if (!file.exists()) {
                System.out.println("本地檔案 " + localPath + " 不存在。");
                return;
            }

            URL url = new URL(baseUrl + remotePath + "?overwrite=" + overwrite);
            HttpURLConnection connection = (HttpURLConnection) url.openConnection();
            connection.setRequestMethod("PUT");
            connection.setRequestProperty("x-isi-ifs-target-type", "object");
            connection.setRequestProperty("Authorization", "Basic " + getBasicAuth());
            connection.setDoOutput(true);

            // 上傳檔案
            try (OutputStream out = connection.getOutputStream();
                 FileInputStream in = new FileInputStream(file)) {
                byte[] buffer = new byte[4096];
                int bytesRead;
                while ((bytesRead = in.read(buffer)) != -1) {
                    out.write(buffer, 0, bytesRead);
                }
            }

            // 發送請求並處理回應
            int responseCode = connection.getResponseCode();
            if (responseCode == 200 || responseCode == 201) {
                System.out.println("檔案 " + remotePath + " 上傳成功。");
            } else {
                System.out.println("上傳檔案失敗，狀態碼：" + responseCode + "，訊息：" + connection.getResponseMessage());
            }
        } catch (IOException e) {
            e.printStackTrace();
        }
    }

    // 取得基本授權（Base64編碼）
    private static String getBasicAuth() {
        String auth = username + ":" + password;
        return Base64.getEncoder().encodeToString(auth.getBytes());
    }

    public static void main(String[] args) {
        // 禁用 SSL 驗證
        disableSSLVerification();

        // 檢查本地檔案是否存在
        File localFile = new File(localFilePath);
        if (!localFile.exists()) {
            System.out.println("本地檔案 " + localFilePath + " 不存在。請確認檔案路徑正確。");
            return;
        }

        // 創建目錄並上傳檔案
        createDirectory(directoryPath);
        uploadFile(remoteFilePath, localFilePath, true);
    }
}

